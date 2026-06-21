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
1. `AKUN-001-ORACLE-VLESS-WS-70MS` (url=251ms, nekobox=267ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=248ms, nekobox=287ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-81MS` (url=246ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=245ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=250ms, nekobox=278ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=243ms, nekobox=297ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=272ms, nekobox=282ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=247ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=251ms, nekobox=278ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS` (url=249ms, nekobox=268ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=241ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-142MS` (url=252ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-282MS` (url=604ms, status=HTTP 204)
14. `AKUN-014-SPEEDTEST-VLESS-WS-298MS` (url=646ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-307MS` (url=609ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-323MS` (url=664ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-315MS` (url=657ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-119MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-272MS` (url=553ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-291MS` (url=669ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-531MS` (url=830ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-570MS` (url=912ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-613MS` (url=3776ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-616MS` (url=1077ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-262MS` (url=4364ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
