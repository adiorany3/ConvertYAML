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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=191ms, nekobox=245ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-63MS` (url=220ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=191ms, nekobox=222ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=214ms, nekobox=178ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-82MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-85MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-70MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-65MS` (url=192ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-81MS` (url=366ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-75MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-346MS` (url=733ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-347MS` (url=781ms, status=HTTP 204)
18. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-403MS` (url=851ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-409MS` (url=847ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-405MS` (url=860ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-369MS` (url=731ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-386MS` (url=834ms, status=HTTP 204)
23. `AKUN-029-UNKNOWN-VLESS-WS-562MS` (url=708ms, status=HTTP 204)
24. `AKUN-033-APPLESERAJ-VLESS-WS-715MS` (url=1001ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-779MS` (url=1219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
