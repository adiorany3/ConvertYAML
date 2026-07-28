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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=200ms, nekobox=224ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=207ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-63MS` (url=204ms, nekobox=223ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=228ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=222ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, nekobox=231ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-68MS` (url=204ms, nekobox=225ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=201ms, nekobox=230ms, status=yes)
9. `AKUN-009-ADF-VLESS-WS-78MS` (url=217ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-86MS` (url=216ms, nekobox=229ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-73MS` (url=229ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-77MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-MYBB-VLESS-WS-96MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-70MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-76MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-69MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-75MS` (url=208ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-78MS` (url=204ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=212ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-103MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-ZVC-VLESS-WS-63MS` (url=209ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-98MS` (url=212ms, status=HTTP 204)
24. `AKUN-024-OVH-VLESS-WS-128MS` (url=216ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-164MS` (url=249ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
