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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-62MS` (url=217ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=224ms, nekobox=254ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS` (url=214ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=221ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=223ms, nekobox=253ms, status=yes)
7. `AKUN-007-NET-NL-VLESS-WS-104MS` (url=205ms, nekobox=241ms, status=yes)
8. `AKUN-008-HOSTOFF-NET-VLESS-WS-115MS` (url=203ms, nekobox=246ms, status=yes)
9. `AKUN-009-SPACECORE-VLESS-WS-94MS` (url=231ms, nekobox=260ms, status=yes)
10. `AKUN-010-U1HOST-FRA-VLESS-WS-81MS` (url=232ms, nekobox=251ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-95MS` (url=231ms, status=HTTP 204)
12. `AKUN-012-OPENAI-VLESS-WS-84MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-115MS` (url=227ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-90MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-116MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-168MS` (url=374ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-84MS` (url=223ms, status=HTTP 204)
18. `AKUN-019-008500-VLESS-WS-85MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-136MS` (url=216ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-236MS` (url=509ms, status=HTTP 204)
21. `AKUN-022-US-VLESS-WS-93MS` (url=222ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-279MS` (url=557ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-270MS` (url=543ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-298MS` (url=601ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-256MS` (url=563ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
