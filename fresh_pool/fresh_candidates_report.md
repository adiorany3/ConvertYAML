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
1. `AKUN-001-UNKNOWN-VLESS-WS-59MS` (url=208ms, nekobox=247ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-57MS` (url=226ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=211ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-126MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-114MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-137MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-132MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS`
11. `AKUN-015-ZVC-VLESS-WS-56MS` (url=226ms, status=HTTP 204)
12. `AKUN-016-CLOUDFLARE-VLESS-WS-65MS` (url=210ms, status=HTTP 204)
13. `AKUN-017-UNKNOWN-VLESS-WS-81MS` (url=219ms, status=HTTP 204)
14. `AKUN-018-UNKNOWN-VLESS-WS-72MS` (url=207ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-80MS` (url=218ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-72MS` (url=197ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-354MS` (url=2391ms, status=HTTP 204)
18. `AKUN-022-RMGYVPN-VLESS-WS-311MS` (url=563ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-334MS` (url=2341ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-391MS` (url=702ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-605MS` (url=1040ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-676MS` (url=1144ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-658MS` (url=1062ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-803MS` (url=1124ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
