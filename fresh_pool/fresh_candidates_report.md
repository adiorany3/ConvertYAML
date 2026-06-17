# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-81MS` (url=231ms, nekobox=257ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS` (url=206ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=205ms, nekobox=234ms, status=yes)
4. `AKUN-004-EGN-22-VLESS-WS-106MS` (url=203ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-107MS` (url=208ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-126MS` (url=202ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-127MS` (url=236ms, nekobox=278ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=213ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-270MS` (url=607ms, nekobox=602ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-293MS` (url=2443ms, nekobox=401ms, status=no)
11. `AKUN-010-UNKNOWN-VLESS-WS-125MS`
12. `AKUN-017-CLOUDFLARE-VLESS-WS-275MS` (url=565ms, status=HTTP 204)
13. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=267ms, status=HTTP 204)
14. `AKUN-021-UNKNOWN-VLESS-WS-503MS` (url=819ms, status=HTTP 204)
15. `AKUN-023-UNKNOWN-VLESS-WS-477MS` (url=743ms, status=HTTP 204)
16. `AKUN-024-UNKNOWN-VLESS-WS-356MS` (url=686ms, status=HTTP 204)
17. `AKUN-026-CLOUDFLARE-VLESS-WS-454MS` (url=771ms, status=HTTP 204)
18. `AKUN-029-CLOUDFLARE-VLESS-WS-280MS` (url=532ms, status=HTTP 204)
19. `AKUN-030-UNKNOWN-VLESS-WS-564MS` (url=2995ms, status=HTTP 204)
20. `AKUN-031-UNKNOWN-VLESS-WS-496MS` (url=811ms, status=HTTP 204)
21. `AKUN-033-JISON-VLESS-WS-411MS` (url=686ms, status=HTTP 204)
22. `AKUN-034-UNKNOWN-VLESS-WS-648MS` (url=1679ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
