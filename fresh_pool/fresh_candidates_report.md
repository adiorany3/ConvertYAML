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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=229ms, nekobox=248ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-59MS` (url=227ms, nekobox=267ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=237ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=223ms, nekobox=259ms, status=yes)
5. `AKUN-005-CHATGPT-VLESS-WS-65MS` (url=226ms, nekobox=269ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=229ms, nekobox=343ms, status=yes)
7. `AKUN-007-NIST-G-VLESS-WS-72MS` (url=245ms, nekobox=267ms, status=yes)
8. `AKUN-008-SPEEDTEST-VLESS-WS-64MS` (url=240ms, nekobox=170ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-116MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-92MS`
12. `AKUN-012-877774-VLESS-WS-93MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-LEVIKOGJGFDD-VLESS-WS-134MS` (url=238ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-129MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-77MS` (url=238ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-116MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-169MS` (url=291ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-77MS` (url=213ms, status=HTTP 204)
19. `AKUN-019-FASTVPSUS-IPV4-VLESS-WS-157MS` (url=327ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-266MS` (url=550ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-379MS` (url=819ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-385MS` (url=752ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-468MS` (url=705ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-516MS` (url=951ms, status=HTTP 204)
25. `AKUN-028-SPEEDTEST-VLESS-WS-548MS` (url=823ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
