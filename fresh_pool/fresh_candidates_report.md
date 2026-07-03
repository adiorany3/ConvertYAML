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
1. `AKUN-001-UNKNOWN-VLESS-WS-81MS` (url=254ms, nekobox=280ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-79MS` (url=262ms, nekobox=280ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=266ms, nekobox=288ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-77MS` (url=243ms, nekobox=291ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=258ms, nekobox=268ms, status=yes)
6. `AKUN-006-WEYRO-NET-VLESS-WS-86MS` (url=262ms, nekobox=293ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-79MS` (url=234ms, nekobox=256ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-84MS` (url=233ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=243ms, nekobox=282ms, status=yes)
10. `AKUN-010-ZVC-VLESS-WS-71MS` (url=242ms, nekobox=262ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-110MS` (url=252ms, status=HTTP 204)
12. `AKUN-012-ALIBABA-VLESS-WS-86MS` (url=241ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-82MS` (url=242ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-132MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-264MS` (url=558ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-285MS` (url=644ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-278MS` (url=591ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-286MS` (url=649ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-290MS` (url=670ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-295MS` (url=545ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-284MS` (url=543ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-158MS` (url=294ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-504MS` (url=811ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-508MS` (url=885ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-812MS` (url=1054ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
