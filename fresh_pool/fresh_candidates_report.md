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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-115MS` (url=302ms, nekobox=321ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-117MS` (url=281ms, nekobox=303ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-114MS` (url=246ms, nekobox=267ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-96MS` (url=292ms, nekobox=274ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-99MS` (url=243ms, nekobox=7171ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=296ms, nekobox=181ms, status=no)
7. `AKUN-005-ZVC-VLESS-WS-120MS`
8. `AKUN-006-1PASSWORD-VLESS-WS-122MS`
9. `AKUN-007-BIGCOMMERCE-VLESS-WS-128MS`
10. `AKUN-010-ZVC-VLESS-WS-117MS` (url=249ms, nekobox=181ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-120MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-117MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-137MS` (url=276ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=259ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=275ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-139MS` (url=226ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-151MS` (url=262ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-118MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-121MS` (url=259ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-124MS` (url=352ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-155MS` (url=285ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-138MS` (url=247ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-123MS` (url=287ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-192MS` (url=408ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
