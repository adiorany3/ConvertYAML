# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-090227-VLESS-WS-63MS` (url=230ms, nekobox=251ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=228ms, nekobox=258ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=208ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=235ms, nekobox=252ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=211ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=237ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=238ms, nekobox=239ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=236ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=232ms, nekobox=178ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=218ms, nekobox=182ms, status=no)
11. `AKUN-011-DEV-VLESS-WS-127MS` (url=234ms, nekobox=184ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-124MS` (url=217ms, nekobox=180ms, status=no)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-122MS` (url=256ms, nekobox=186ms, status=no)
14. `AKUN-015-SPEEDTEST-VLESS-WS-123MS` (url=234ms, nekobox=189ms, status=no)
15. `AKUN-016-SPEEDTEST-VLESS-WS-158MS` (url=268ms, nekobox=289ms, status=no)
16. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
17. `AKUN-010-CLOUDFLARE-VLESS-WS-404MS`
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-432MS` (url=852ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-397MS` (url=881ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-440MS` (url=891ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-358MS` (url=765ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-425MS` (url=869ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-367MS` (url=801ms, status=HTTP 204)
24. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-760MS` (url=966ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
