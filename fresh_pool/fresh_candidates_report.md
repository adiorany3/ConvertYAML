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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-ZOOM-VLESS-WS-90MS` (url=222ms, nekobox=259ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-84MS` (url=201ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=390ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-118MS` (url=199ms, nekobox=261ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=223ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-128MS` (url=210ms, nekobox=205ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
8. `AKUN-007-ES-FORNEX-20160629-VLESS-WS-97MS`
9. `AKUN-008-DIGITALOCEAN-VLESS-WS-93MS`
10. `AKUN-009-LEVIKOGJGFDD-VLESS-WS-203MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-253MS`
12. `AKUN-012-INTERNETWORKS-45-131-210-VLESS-WS-253MS` (url=522ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-240MS` (url=516ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-284MS` (url=1617ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-265MS` (url=2789ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-267MS` (url=2505ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-255MS` (url=517ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-415MS` (url=502ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-417MS` (url=519ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-82MS` (url=220ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-94MS` (url=205ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-425MS` (url=523ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-483MS` (url=763ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-469MS` (url=894ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-427MS` (url=507ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
