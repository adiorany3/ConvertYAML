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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=199ms, nekobox=228ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-60MS` (url=208ms, nekobox=224ms, status=yes)
3. `AKUN-003-ZOOM-VLESS-WS-73MS` (url=209ms, nekobox=220ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=220ms, nekobox=227ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-69MS` (url=217ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, nekobox=178ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-77MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-104MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-70MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-121MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-090227-VLESS-WS-131MS` (url=339ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-153MS` (url=251ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-214MS` (url=290ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-278MS` (url=576ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-372MS` (url=604ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-436MS` (url=633ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-323MS` (url=689ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-432MS` (url=1615ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-452MS` (url=680ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-391MS` (url=658ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-503MS` (url=843ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-508MS` (url=842ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
