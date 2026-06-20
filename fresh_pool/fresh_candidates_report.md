# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-UNKNOWN-VLESS-WS-71MS` (url=286ms, nekobox=234ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS` (url=201ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-84MS` (url=221ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS` (url=212ms, nekobox=249ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-63MS` (url=205ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=202ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=218ms, nekobox=247ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-241MS` (url=510ms, nekobox=536ms, status=yes)
10. `AKUN-010-SPEEDTEST-VLESS-WS-230MS` (url=526ms, nekobox=545ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-275MS` (url=574ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-293MS` (url=585ms, status=HTTP 204)
13. `AKUN-014-WPENG-VLESS-WS-272MS` (url=586ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-262MS` (url=251ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-391MS` (url=585ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-292MS` (url=592ms, status=HTTP 204)
17. `AKUN-021-BROADNNET-KR-VLESS-WS-449MS` (url=569ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-380MS` (url=927ms, status=HTTP 204)
19. `AKUN-034-SOLTANKABOS-VLESS-WS-652MS` (url=1240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
