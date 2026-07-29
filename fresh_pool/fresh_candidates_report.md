# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-92MS` (url=347ms, nekobox=278ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS` (url=279ms, nekobox=227ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-111MS`
4. `AKUN-003-BIGCOMMERCE-VLESS-WS-112MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-100MS`
6. `AKUN-005-DEV-VLESS-WS-92MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=327ms, nekobox=199ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS`
12. `AKUN-010-HOSTINGER-VLESS-WS-117MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-117MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=263ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=267ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=246ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=266ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-111MS` (url=243ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-120MS` (url=259ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-125MS` (url=276ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-166MS` (url=337ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-181MS` (url=363ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-166MS` (url=389ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
