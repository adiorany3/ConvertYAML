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
1. `AKUN-001-US-VLESS-WS-76MS` (url=235ms, nekobox=280ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-76MS` (url=265ms, nekobox=272ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=243ms, nekobox=264ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-79MS` (url=230ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=249ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=248ms, nekobox=266ms, status=yes)
7. `AKUN-007-DIGITALOCEAN-VLESS-WS-74MS` (url=257ms, nekobox=269ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS` (url=244ms, nekobox=278ms, status=yes)
9. `AKUN-009-U1HOST-FRA-VLESS-WS-76MS` (url=247ms, nekobox=265ms, status=yes)
10. `AKUN-010-1PASSWORD-VLESS-WS-86MS` (url=259ms, nekobox=267ms, status=yes)
11. `AKUN-011-NETCUP-VLESS-WS-82MS` (url=273ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-82MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-NET-NL-VLESS-WS-69MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-71MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-72MS` (url=254ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-91MS` (url=267ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-108MS` (url=232ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-96MS` (url=265ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=233ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-258MS` (url=593ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-304MS` (url=623ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-312MS` (url=662ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-325MS` (url=662ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-294MS` (url=648ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
