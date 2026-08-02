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
1. `AKUN-001-UNKNOWN-VLESS-WS-75MS` (url=398ms, nekobox=347ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-100MS` (url=328ms, nekobox=427ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-101MS` (url=415ms, nekobox=330ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-132MS` (url=402ms, nekobox=355ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-153MS` (url=367ms, nekobox=316ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-156MS` (url=383ms, nekobox=417ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-136MS` (url=412ms, nekobox=365ms, status=yes)
8. `AKUN-008-LEVIKOGJGFDD-VLESS-WS-158MS` (url=313ms, nekobox=317ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-140MS` (url=294ms, nekobox=391ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-168MS` (url=354ms, nekobox=334ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-171MS` (url=438ms, status=HTTP 204)
12. `AKUN-012-RMGYVPN-VLESS-WS-200MS` (url=521ms, status=HTTP 204)
13. `AKUN-013-LT-LRTC-20060503-VLESS-WS-173MS` (url=393ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-154MS` (url=711ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-339MS` (url=668ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-472MS` (url=896ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-462MS` (url=963ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-509MS` (url=1011ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-524MS` (url=801ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-505MS` (url=1060ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-550MS` (url=885ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-545MS` (url=911ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-566MS` (url=881ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-586MS` (url=1434ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-668MS` (url=1868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
