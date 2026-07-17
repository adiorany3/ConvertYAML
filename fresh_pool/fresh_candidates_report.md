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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=330ms, nekobox=398ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-102MS` (url=420ms, nekobox=363ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-112MS` (url=446ms, nekobox=567ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-119MS` (url=308ms, nekobox=329ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-114MS` (url=324ms, nekobox=318ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS` (url=336ms, nekobox=334ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS` (url=342ms, nekobox=339ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS` (url=371ms, nekobox=311ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS` (url=297ms, nekobox=387ms, status=yes)
10. `AKUN-010-CZ-LOTUNA-19970206-VLESS-WS-124MS` (url=315ms, nekobox=392ms, status=yes)
11. `AKUN-011-MYBB-VLESS-WS-136MS` (url=274ms, status=HTTP 204)
12. `AKUN-012-DIXONS-VLESS-WS-128MS` (url=301ms, status=HTTP 204)
13. `AKUN-013-SPEEDTEST-VLESS-WS-115MS` (url=321ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-158MS` (url=313ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-141MS` (url=328ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-135MS` (url=270ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-147MS` (url=350ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-187MS` (url=347ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-137MS` (url=306ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-340MS` (url=731ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-343MS` (url=656ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-318MS` (url=677ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-345MS` (url=762ms, status=HTTP 204)
24. `AKUN-028-WPENG-VLESS-WS-101MS` (url=336ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-535MS` (url=801ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
