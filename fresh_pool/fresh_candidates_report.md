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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-87MS` (url=203ms, nekobox=230ms, status=yes)
2. `AKUN-002-GOV-VLESS-WS-87MS` (url=211ms, nekobox=236ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-93MS` (url=267ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=277ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=234ms, nekobox=238ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=238ms, nekobox=232ms, status=yes)
7. `AKUN-007-SAVVY-7-VLESS-WS-102MS` (url=212ms, nekobox=248ms, status=yes)
8. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-101MS` (url=220ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=207ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-89MS` (url=205ms, nekobox=232ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=247ms, status=HTTP 204)
13. `AKUN-013-US-VLESS-WS-120MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-103MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-126MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-109MS` (url=255ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-118MS` (url=227ms, status=HTTP 204)
18. `AKUN-018-POLICE-VLESS-WS-110MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-133MS` (url=220ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-113MS` (url=214ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-113MS` (url=239ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-114MS` (url=228ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-105MS` (url=255ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-164MS` (url=213ms, status=HTTP 204)
25. `AKUN-025-WEBEX-VLESS-WS-91MS` (url=214ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
