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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-67MS` (url=229ms, nekobox=242ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-69MS` (url=236ms, nekobox=242ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-60MS` (url=267ms, nekobox=267ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS` (url=227ms, nekobox=7177ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-94MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
10. `AKUN-009-466688-VLESS-WS-71MS`
11. `AKUN-011-DEV-VLESS-WS-77MS` (url=251ms, nekobox=183ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-99MS` (url=233ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-107MS` (url=281ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-114MS` (url=249ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-TENCENT-VLESS-WS-94MS` (url=264ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-108MS` (url=289ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-98MS` (url=247ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-106MS` (url=264ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-273MS` (url=470ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-365MS` (url=1761ms, status=HTTP 204)
24. `AKUN-026-PUBLICDOMAINREGISTRY-NET-VLESS-WS-406MS` (url=838ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-434MS` (url=890ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
