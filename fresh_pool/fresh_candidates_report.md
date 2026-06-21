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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=223ms, nekobox=179ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS`
4. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-74MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-77MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS`
7. `AKUN-006-VULTR-VLESS-WS-87MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-96MS`
10. `AKUN-009-VULTR-VLESS-WS-108MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS`
12. `AKUN-012-CONFLU-VLESS-WS-231MS` (url=480ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-246MS` (url=594ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-248MS` (url=556ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-252MS` (url=525ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-265MS` (url=560ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-264MS` (url=520ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-305MS` (url=547ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-345MS` (url=450ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-492MS` (url=797ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-199MS` (url=804ms, status=HTTP 204)
22. `AKUN-031-UNKNOWN-VLESS-WS-466MS` (url=468ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-553MS` (url=956ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-620MS` (url=2374ms, status=HTTP 204)
25. `AKUN-035-DEV-VLESS-WS-678MS` (url=756ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
