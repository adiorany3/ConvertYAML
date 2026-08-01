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
1. `AKUN-001-UNKNOWN-VLESS-WS-84MS` (url=208ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS` (url=237ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=205ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=235ms, nekobox=263ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=235ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=234ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=223ms, nekobox=240ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS` (url=227ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=236ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, nekobox=200ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-115MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=212ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-121MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=317ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-128MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-137MS` (url=268ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-149MS` (url=213ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-192MS` (url=238ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-327MS` (url=676ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-310MS` (url=613ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-629MS` (url=1024ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-672MS` (url=1096ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-815MS` (url=1622ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-840MS` (url=1333ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-875MS` (url=3285ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
