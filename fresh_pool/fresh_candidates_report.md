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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=213ms, nekobox=252ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=230ms, nekobox=180ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=225ms, nekobox=187ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS`
10. `AKUN-008-ZVC-VLESS-WS-71MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-76MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-84MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-88MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-93MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-76MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-85MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-MYBB-VLESS-WS-97MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-99MS` (url=216ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-91MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-99MS` (url=296ms, status=HTTP 204)
24. `AKUN-024-LEVIKOGJGFDD-VLESS-WS-246MS` (url=499ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-268MS` (url=508ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
