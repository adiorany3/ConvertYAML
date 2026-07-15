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
1. `AKUN-001-CZ-LOTUNA-19970206-VLESS-WS-92MS` (url=309ms, nekobox=339ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-98MS` (url=213ms, nekobox=467ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-97MS` (url=236ms, nekobox=276ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-100MS` (url=233ms, nekobox=267ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-106MS` (url=244ms, nekobox=241ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-118MS` (url=256ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-120MS` (url=248ms, nekobox=327ms, status=yes)
8. `AKUN-008-US-VLESS-WS-123MS` (url=284ms, nekobox=326ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-103MS` (url=240ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=221ms, nekobox=268ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-117MS` (url=265ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=287ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-139MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-111MS` (url=225ms, status=HTTP 204)
16. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-127MS` (url=266ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-137MS` (url=286ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=255ms, status=HTTP 204)
19. `AKUN-020-DIXONS-VLESS-WS-127MS` (url=251ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-128MS` (url=355ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-388MS` (url=5080ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-415MS` (url=858ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-402MS` (url=906ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-411MS` (url=3261ms, status=HTTP 204)
25. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-446MS` (url=911ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
