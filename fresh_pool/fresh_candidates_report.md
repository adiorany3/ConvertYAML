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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-92MS` (url=207ms, nekobox=296ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS` (url=206ms, nekobox=239ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-96MS` (url=210ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-88MS` (url=211ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=204ms, nekobox=236ms, status=yes)
6. `AKUN-006-CCWU-VLESS-WS-101MS` (url=240ms, nekobox=250ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-106MS` (url=230ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-103MS` (url=241ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=216ms, nekobox=255ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=234ms, nekobox=259ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-115MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-119MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-116MS` (url=241ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-123MS` (url=279ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-128MS` (url=273ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-126MS` (url=253ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-116MS` (url=247ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-93MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-153MS` (url=262ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-146MS` (url=284ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-113MS` (url=235ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-162MS` (url=258ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-103MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
