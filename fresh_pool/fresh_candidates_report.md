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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=201ms, nekobox=229ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-95MS` (url=201ms, nekobox=235ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=214ms, nekobox=231ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-91MS` (url=198ms, nekobox=236ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-90MS` (url=212ms, nekobox=251ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-90MS` (url=244ms, nekobox=251ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-102MS` (url=239ms, nekobox=278ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-107MS` (url=204ms, nekobox=245ms, status=yes)
9. `AKUN-009-DEV-VLESS-WS-106MS` (url=212ms, nekobox=203ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-145MS`
12. `AKUN-012-LEVIKOGJGFDD-VLESS-WS-127MS` (url=217ms, status=HTTP 204)
13. `AKUN-013-FASTVPSUS-IPV4-VLESS-WS-190MS` (url=323ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=286ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-176MS` (url=375ms, status=HTTP 204)
16. `AKUN-017-DE-CLOUDKLEYER-20190515-VLESS-WS-172MS` (url=272ms, status=HTTP 204)
17. `AKUN-018-RMGYVPN-VLESS-WS-300MS` (url=637ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-149MS` (url=397ms, status=HTTP 204)
19. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-171MS` (url=347ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-635MS` (url=1034ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-694MS` (url=1198ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-693MS` (url=1230ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-707MS` (url=1562ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-706MS` (url=1153ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-723MS` (url=1106ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
