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
1. `AKUN-001-SPEEDTEST-VLESS-WS-61MS` (url=218ms, nekobox=175ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS`
5. `AKUN-005-SPEEDTEST-VLESS-WS-67MS` (url=217ms, nekobox=174ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-59MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-68MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-59MS` (url=208ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-57MS` (url=203ms, nekobox=173ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-64MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-58MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-63MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-77MS`
14. `AKUN-014-FASTVPSUS-IPV4-VLESS-WS-70MS` (url=238ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-76MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-55MS` (url=207ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-70MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-276MS` (url=557ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-511MS` (url=1025ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-532MS` (url=1029ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-524MS` (url=1023ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-491MS` (url=1103ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-626MS` (url=1325ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-596MS` (url=1035ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
