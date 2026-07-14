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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-102MS` (url=304ms, nekobox=353ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-117MS` (url=321ms, nekobox=310ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-125MS` (url=285ms, nekobox=329ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=316ms, nekobox=343ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-134MS` (url=372ms, nekobox=485ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-134MS` (url=336ms, nekobox=345ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-135MS` (url=353ms, nekobox=397ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-153MS` (url=342ms, nekobox=324ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=324ms, nekobox=343ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-156MS` (url=344ms, nekobox=342ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-145MS` (url=349ms, status=HTTP 204)
12. `AKUN-012-IDC-SG-VLESS-WS-147MS` (url=323ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-125MS` (url=303ms, status=HTTP 204)
14. `AKUN-014-CZ-LOTUNA-19970206-VLESS-WS-129MS` (url=324ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-134MS` (url=331ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-147MS` (url=427ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-157MS` (url=320ms, status=HTTP 204)
18. `AKUN-018-CZ-LOTUNA-19970206-VLESS-WS-133MS` (url=331ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-200MS` (url=382ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-231MS` (url=390ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-297MS` (url=670ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-182MS` (url=352ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-322MS` (url=636ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-325MS` (url=635ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-307MS` (url=641ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
