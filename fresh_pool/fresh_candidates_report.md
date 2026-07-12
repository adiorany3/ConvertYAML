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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=239ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=237ms, nekobox=263ms, status=yes)
3. `AKUN-003-OVH-VLESS-WS-69MS` (url=232ms, nekobox=265ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=232ms, nekobox=275ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-65MS` (url=231ms, nekobox=273ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-69MS` (url=281ms, nekobox=263ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-76MS` (url=283ms, nekobox=266ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=221ms, nekobox=268ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=225ms, nekobox=270ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=249ms, nekobox=260ms, status=yes)
11. `AKUN-011-NODEHOST-VLESS-WS-89MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=243ms, status=HTTP 204)
13. `AKUN-013-ORG-VLESS-WS-93MS` (url=239ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=246ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-92MS` (url=233ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=231ms, status=HTTP 204)
17. `AKUN-018-CONFLU-VLESS-WS-247MS` (url=609ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-292MS` (url=2867ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-298MS` (url=656ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-235MS` (url=554ms, status=HTTP 204)
21. `AKUN-025-QZZ-VLESS-WS-197MS` (url=690ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-447MS` (url=825ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-546MS` (url=894ms, status=HTTP 204)
24. `AKUN-029-SPEEDTEST-VLESS-WS-498MS` (url=835ms, status=HTTP 204)
25. `AKUN-030-GAMEFICTOINSPEED-VLESS-WS-571MS` (url=847ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
