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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=213ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=237ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=230ms, nekobox=271ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=216ms, nekobox=280ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=237ms, nekobox=243ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-96MS` (url=224ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=216ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-94MS` (url=342ms, nekobox=302ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=237ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=229ms, nekobox=261ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-84MS` (url=266ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-104MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-95MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-176MS` (url=278ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-265MS` (url=812ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-354MS` (url=753ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-384MS` (url=805ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-397MS` (url=811ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-392MS` (url=826ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-396MS` (url=1770ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-358MS` (url=787ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-69MS` (url=728ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-68MS` (url=581ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-599MS` (url=551ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
