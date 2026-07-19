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
1. `AKUN-001-RU-BEGET-VLESS-WS-87MS` (url=202ms, nekobox=276ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-90MS` (url=207ms, nekobox=262ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-94MS` (url=368ms, nekobox=240ms, status=yes)
4. `AKUN-004-ORG-VLESS-WS-93MS` (url=230ms, nekobox=284ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-96MS` (url=210ms, nekobox=260ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-90MS` (url=209ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=220ms, nekobox=7177ms, status=no)
8. `AKUN-007-SAVVY-7-VLESS-WS-90MS`
9. `AKUN-008-RTCOMM-SRAVNI-RU-VLESS-WS-96MS`
10. `AKUN-009-WPENG-VLESS-WS-96MS`
11. `AKUN-010-UK-GB-DCL-01-20191003-VLESS-WS-94MS`
12. `AKUN-012-ZVC-VLESS-WS-89MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=240ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-98MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-108MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-90MS` (url=204ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-112MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-103MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-104MS` (url=202ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-107MS` (url=220ms, status=HTTP 204)
23. `AKUN-023-VOV-VLESS-WS-114MS` (url=249ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-114MS` (url=226ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-128MS` (url=297ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
