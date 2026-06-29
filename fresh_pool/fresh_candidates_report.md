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
1. `AKUN-001-VULTR-VLESS-WS-74MS` (url=210ms, nekobox=239ms, status=yes)
2. `AKUN-002-COMPREND-NET-VLESS-WS-85MS` (url=268ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-109MS` (url=210ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-114MS` (url=195ms, nekobox=247ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-104MS` (url=210ms, nekobox=248ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=216ms, nekobox=237ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-120MS` (url=203ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-117MS` (url=261ms, nekobox=257ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-91MS` (url=217ms, nekobox=247ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-125MS` (url=214ms, nekobox=234ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-122MS` (url=202ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-150MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-76MS` (url=243ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-92MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-US-VLESS-WS-95MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-229MS` (url=503ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-237MS` (url=3504ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-266MS` (url=572ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-257MS` (url=575ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-270MS` (url=600ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-257MS` (url=497ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-279MS` (url=588ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-303MS` (url=551ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-500MS` (url=834ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-506MS` (url=867ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
