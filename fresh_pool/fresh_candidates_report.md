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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=222ms, nekobox=242ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-66MS` (url=215ms, nekobox=263ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=232ms, nekobox=254ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-61MS` (url=285ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, nekobox=241ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-81MS` (url=281ms, nekobox=264ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=224ms, nekobox=248ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-78MS` (url=268ms, nekobox=181ms, status=no)
9. `AKUN-008-WPENG-VLESS-WS-108MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=239ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-82MS` (url=244ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-113MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-160MS` (url=251ms, status=HTTP 204)
17. `AKUN-017-ADF-VLESS-WS-103MS` (url=251ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-145MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-74MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-82MS` (url=223ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-214MS` (url=391ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-124MS` (url=414ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-289MS` (url=717ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-241MS` (url=554ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-345MS` (url=775ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
